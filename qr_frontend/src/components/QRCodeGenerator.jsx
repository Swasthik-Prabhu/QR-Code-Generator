import { useState } from "react";
import axios from "axios";

export default function QRCodeGenerator() {
  const [link, setLink] = useState("");
  const [qrData, setQrData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerateQR = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/generate/", { link });
      setQrData(response.data);
    } catch (err) {
      setError("Failed to generate QR code. Try again.");
    }

    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-md w-96 text-center">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">QR Code Generator</h2>

        <input
          type="text"
          placeholder="Enter your link"
          value={link}
          onChange={(e) => setLink(e.target.value)}
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
        />

        <button
          onClick={handleGenerateQR}
          className={`mt-4 w-full px-4 py-2 rounded text-white font-bold transition ${
            loading ? "bg-gray-400 cursor-not-allowed" : "bg-blue-500 hover:bg-blue-600"
          }`}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate QR Code"}
        </button>

        {error && <p className="text-red-500 mt-2">{error}</p>}

        {qrData && (
          <div className="mt-4">
            <p className="text-green-600 font-semibold">QR Code Generated!</p>
            <img src={`http://127.0.0.1:8000${qrData.download_url}`} alt="QR Code" className="w-40 mx-auto" />
            <a
              href={`http://127.0.0.1:8000${qrData.download_url}`}
              download
              className="block mt-2 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
            >
              Download QR Code
            </a>
          </div>
        )}
      </div>
    </div>
  );
}
