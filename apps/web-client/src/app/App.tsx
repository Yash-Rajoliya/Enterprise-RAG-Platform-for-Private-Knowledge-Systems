import { BrowserRouter } from "react-router-dom";
import RoutesApp from "./routes";
import Providers from "./providers";

export default function App() {
 return (
  <BrowserRouter>
   <Providers>
    <RoutesApp />
   </Providers>
  </BrowserRouter>
 );
}