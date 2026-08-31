import {
 Routes,
 Route
} from "react-router-dom";

import ChatPage from "../pages/ChatPage";
import UploadPage from "../pages/UploadPage";
import HistoryPage from "../pages/HistoryPage";
import LoginPage from "../pages/LoginPage";
import NotFound from "../pages/NotFound";

export default function RoutesApp() {
 return (
  <Routes>
   <Route path="/" element={<ChatPage />} />
   <Route path="/upload" element={<UploadPage />} />
   <Route path="/history" element={<HistoryPage />} />
   <Route path="/login" element={<LoginPage />} />
   <Route path="*" element={<NotFound />} />
  </Routes>
 );
}