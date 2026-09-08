export async function apiFetch(token, ruta, opciones = {}) {
    const response = await fetch(ruta, {
        ...opciones,                              // spread: copia las opciones que le pases
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',    // siempre JSON por defecto
            ...opciones.headers                    // permite sobreescribir headers específicos
        }
    })

    if (!response.ok) {
        const error = await response.json().catch(() => ({ detail: 'Error del servidor' }))
        throw new Error(error.detail || `Error ${response.status}`)
    }

    // 204 No Content (DELETE exitoso) no tiene body
    if (response.status === 204) return null

    return response.json()
}

export async function verUsuario(token){
    const response = await fetch('/auth/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }       
    });

    const data = await response.json();

    return { data, token }
}