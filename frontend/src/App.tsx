import { useState, useEffect } from 'react'

function App() {
    const [status, setStatus] = useState<string>('Loading...')

    useEffect(() => {
        fetch('http://localhost:8000/health')
            .then(res => res.json())
            .then(data => setStatus(data.status))
            .catch(err => setStatus('Error connecting to backend'))
    }, [])

    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">
            <div className="bg-white p-8 rounded-lg shadow-md">
                <h1 className="text-3xl font-bold text-blue-600 mb-4">NOVA Learning Platform</h1>
                <p className="text-gray-700">Backend Status: <span className="font-semibold">{status}</span></p>
            </div>
        </div>
    )
}

export default App
