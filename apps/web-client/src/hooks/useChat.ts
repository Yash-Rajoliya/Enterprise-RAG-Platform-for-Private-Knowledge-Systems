import { useState } from "react";

export function useChat(){
 const [messages,setMessages]=useState<any[]>([]);

 const send=(msg:string)=>{
  setMessages([...messages,msg]);
 };

 return {messages,send};
}