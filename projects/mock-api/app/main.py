from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(
    title="Mock API Laboratorio",
    description="API simulada para probar automatismos locales",
    version="1.0.0",
)

# ==========================================================
# MODELOS
# ==========================================================

class SaldoResponse(BaseModel):
    msisdn: str
    saldo: float
    estado: str
    timestamp: str


class RecargaRequest(BaseModel):
    msisdn: str
    amount: float
    reason: Optional[str] = "Mock recarga"


class BonoRequest(BaseModel):
    msisdn: str
    product_offering_id: str
    sales_person_id: Optional[str] = "MOCK"


# ==========================================================
# DATOS MOCK EN MEMORIA
# ==========================================================

SALDOS = {
    "600000001": 10.50,
    "600000002": 0.10,
    "600000003": 0.00,
    "600000004": 15.00,
}

BONOS_ACTIVOS = {
    "600000004": ["PO_TODO_INCLUIDO_15_Lebara"]
}


# ==========================================================
# ENDPOINTS BASE
# ==========================================================

@app.get("/")
def root():
    return {
        "service": "mock-api",
        "status": "OK",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "timestamp": datetime.now().isoformat()
    }


# ==========================================================
# MOCK SALDO
# ==========================================================

@app.get("/saldo/{msisdn}", response_model=SaldoResponse)
def consultar_saldo(msisdn: str):
    saldo = SALDOS.get(msisdn)

    if saldo is None:
        raise HTTPException(
            status_code=404,
            detail=f"MSISDN {msisdn} no encontrado"
        )

    return {
        "msisdn": msisdn,
        "saldo": saldo,
        "estado": "OK",
        "timestamp": datetime.now().isoformat()
    }


# ==========================================================
# MOCK RECARGA
# ==========================================================

@app.post("/recarga")
def recargar(payload: RecargaRequest):
    saldo_actual = SALDOS.get(payload.msisdn, 0.0)
    nuevo_saldo = round(saldo_actual + payload.amount, 2)
    SALDOS[payload.msisdn] = nuevo_saldo

    return {
        "estado": "OK",
        "mensaje": "Recarga simulada correctamente",
        "msisdn": payload.msisdn,
        "saldo_anterior": saldo_actual,
        "importe_recarga": payload.amount,
        "saldo_nuevo": nuevo_saldo,
        "reason": payload.reason,
        "timestamp": datetime.now().isoformat()
    }


# ==========================================================
# MOCK BONO
# ==========================================================

@app.post("/bono")
def activar_bono(payload: BonoRequest):
    bonos = BONOS_ACTIVOS.setdefault(payload.msisdn, [])

    if payload.product_offering_id in bonos:
        return {
            "estado": "YA_EXISTE",
            "mensaje": "El bono ya estaba activo",
            "msisdn": payload.msisdn,
            "product_offering_id": payload.product_offering_id,
            "timestamp": datetime.now().isoformat()
        }

    bonos.append(payload.product_offering_id)

    return {
        "estado": "OK",
        "mensaje": "Bono activado correctamente",
        "msisdn": payload.msisdn,
        "product_offering_id": payload.product_offering_id,
        "sales_person_id": payload.sales_person_id,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/bono/{msisdn}")
def consultar_bonos(msisdn: str):
    return {
        "msisdn": msisdn,
        "bonos_activos": BONOS_ACTIVOS.get(msisdn, []),
        "timestamp": datetime.now().isoformat()
    }
