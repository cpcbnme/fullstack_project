export const runtime = 'edge'

export async function POST(req: Request) {
    const res = await fetch('http://localhost:8000/orders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: req.body,
    })

    const data = await res.json()

    return Response.json(data)
}