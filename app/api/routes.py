from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
import uuid
import os

from app.services.data_cleaner import clean_data
from app.services.reconciliation_service import reconcile_data
from app.services.schema_mapper import normalize_columns, validate_schema
from app.services.data_loader import load_file

router = APIRouter()

@router.post("/reconcile/")
async def reconcile(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    
    # Read uploaded files
    df1 = pd.load_file(file1.file)
    df2 = pd.load_file(file2.file)

    # Clean data
    df1 = clean_data(df1)
    df2 = clean_data(df2)

    # Reconcile
    result = reconcile_data(df1, df2)

    # Return summary (not full data yet)
    summary = {key: len(value) for key, value in result.items()}

    return {
        "message": "Reconciliation completed",
        "summary": summary
    }
    
@router.post("/reconcile/download/")
async def reconcile_and_download(file1: UploadFile = File(...), file2: UploadFile = File(...)):

    df1 = pd.load_file(file1.file)
    df2 = pd.load_file(file2.file)

    df1 = clean_data(df1)
    df2 = clean_data(df2)

    result = reconcile_data(df1, df2)
    os.makedirs("reports", exist_ok=True)

    # Unique filename
    filename = f"reports/reconciliation_{uuid.uuid4().hex}.xlsx"

    # Generate report
    from app.services.report_service import generate_excel_report
    generate_excel_report(result, filename)

    return FileResponse(
        path=filename,
        filename="reconciliation_report.xlsx",
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    
@router.post("/reconcile/dynamic/")
async def reconcile_dynamic(file1: UploadFile = File(...), file2: UploadFile = File(...)):

    try:
        df1 = load_file(file1)
        df2 = load_file(file2)

        # Normalize
        df1 = normalize_columns(df1)
        df2 = normalize_columns(df2)

        # Validate schema (based on required fields)
        validate_schema(df1)
        validate_schema(df2)

        # Clean
        df1 = clean_data(df1)
        df2 = clean_data(df2)

        # Reconcile
        result = reconcile_data(df1, df2)
        os.makedirs("reports", exist_ok=True)

        # Unique filename
        filename = f"reports/reconciliation_{uuid.uuid4().hex}.xlsx"

        # Generate report
        from app.services.report_service import generate_excel_report
        generate_excel_report(result, filename)

        return FileResponse(
            path=filename,
            filename="reconciliation_report.xlsx",
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))