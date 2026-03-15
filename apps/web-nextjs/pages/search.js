import { useState } from 'react';

export default function Search() {
  const [q, setQ] = useState('');
  const [result, setResult] = useState(null);

  async function submit() {
    const res = await fetch('/api/nlp', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({text: q})
    });
    const data = await res.json();
    setResult(data);
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Search</h1>
      <textarea value={q} onChange={e=>setQ(e.target.value)} className="w-full h-24" />
      <button onClick={submit} className="mt-2 px-4 py-2 bg-blue-600 text-white">Submit</button>
      <pre className="mt-4">{result && JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}
