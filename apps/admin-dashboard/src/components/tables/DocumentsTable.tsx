const docs = [
 "contract.pdf",
 "manual.docx",
 "architecture.pdf"
];

export default function DocumentsTable() {
 return (
  <table>
   <tbody>
    {docs.map((d)=>(
     <tr key={d}>
      <td>{d}</td>
     </tr>
    ))}
   </tbody>
  </table>
 );
}