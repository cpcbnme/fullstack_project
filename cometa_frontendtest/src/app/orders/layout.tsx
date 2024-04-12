export default function LayoutStock({children}: {children: React.ReactNode}) {
    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
            <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex-col">
                <h1 className={"font-bold text-3xl"}>Orders</h1>
                <div className={"mt-6"}>
                    {children}
                </div>
            </div>
        </main>
    )
}