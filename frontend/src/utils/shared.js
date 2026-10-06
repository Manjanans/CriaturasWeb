import { useAuthStore } from "@/stores/authStore"

export async function apiFetch(ruta, opciones = {}) {
    const token = useAuthStore().accessToken;

    const response = await fetch(ruta, {
        ...opciones,                              // spread: copia las opciones que le pases
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',    // siempre JSON por defecto
            ...opciones.headers                    // permite sobreescribir headers específicos
        }
    })

    if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail.message)
    }

    // 204 No Content (DELETE exitoso) no tiene body
    if (response.status === 204) return null

    return response.json()
}
