import { useState } from "react";
import { useChat } from "../../hooks/useChat";

export default function PromptInput() {
 const [value,setValue]=useState("");
 const { send }=useChat();

 return (
  <input
   value={value}
   onChange={e=>setValue(e.target.value)}
   onKeyDown={e=>{
    if(e.key==="Enter"){
     send(value);
     setValue("");
    }
   }}
  />
 );
}