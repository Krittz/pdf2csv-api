from fastapi import FastAPI, UploadFile, Query
from fastapi.responses import StreamingResponse, JSONResponse
import pdfplumber
import pandas as pd
from io import BytesIO

app = FastAPI(title="PDF to CSV API")

def make_unique_columns(columns):
    seen = {}
    new_cols = []
    for col in columns:
        if col in seen:
            seen[col] += 1
            new_cols.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            new_cols.append(col if col else f"Unnamed_{len(new_cols)}")
    return new_cols

@app.post("/convert")
async def convert_pdf(
    file: UploadFile,
    col_idx: list[int] = Query(None, description="Índices das colunas desejadas (ex: 0,1,4)")
):
    try:
        pdf = pdfplumber.open(BytesIO(await file.read()))
        all_tables = []

        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table and len(table) > 1:
                    cols = make_unique_columns(table[0])
                    d = pd.DataFrame(table[1:], columns=cols)

                    # 🔹 Se índices de colunas foram passados
                    if col_idx:
                        try:
                            d = d.iloc[:, col_idx]
                        except Exception as e:
                            return JSONResponse(
                                status_code=400,
                                content={"error": f"Índices inválidos: {col_idx}. Detalhe: {str(e)}"}
                            )

                    all_tables.append(d)
                    print(f"[DEBUG] Página {page.page_number}, colunas finais: {list(d.columns)}")

        pdf.close()

        if not all_tables:
            return JSONResponse(
                status_code=400,
                content={"error": "Nenhuma tabela encontrada no PDF"}
            )

        final_df = pd.concat(all_tables, ignore_index=True)

        print(f"[DEBUG] DataFrame final, shape: {final_df.shape}")

        output = BytesIO()
        final_df.to_csv(output, index=False)
        output.seek(0)

        return StreamingResponse(
            output,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=result.csv"}
        )
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
