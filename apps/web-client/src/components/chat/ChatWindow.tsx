import { useChat } from "../../hooks/useChat";

export default function ChatWindow() {
 const { messages } = useChat();

 return (
  <div>
   {messages.map((m:any,i:number)=>(
    <div key={i}>{m}</div>
   ))}
  </div>
 );
}