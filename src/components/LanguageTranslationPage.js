import React from "react";

function LanguageTranslationPage() {
  return (
    <div className="language-translation-page">
      <h1>Language Translation</h1>
      <div className="translation-container">
        <p>Click mic icon for input and select the desired language.</p>
        <div>
          <button>🎤 Speak</button>
          <select>
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="es">Spanish</option>
            {/* Add more languages */}
          </select>
        </div>
        <h3>Translated Text:</h3>
        <p>Translated audio/text will appear here...</p>
      </div>
    </div>
  );
}

export default LanguageTranslationPage;