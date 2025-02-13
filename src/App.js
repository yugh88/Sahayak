import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import SignLanguagePage from "./components/SignLanguagePage";
import EnvironmentDetectionPage from "./components/EnvironmentDetectionPage";
import LanguageTranslationPage from "./components/LanguageTranslationPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-language" element={<SignLanguagePage />} />
        <Route path="/environment-detection" element={<EnvironmentDetectionPage />} />
        <Route path="/language-translation" element={<LanguageTranslationPage />} />
      </Routes>
    </Router>
  );
}

export default App;