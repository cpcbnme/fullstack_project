export async function GET() {
    const res = await fetch('http://localhost:8000/beers', {
        headers: {
            'Content-Type': 'application/json',
        },
    })
    const data = await res.json()

    return Response.json({ data })
}