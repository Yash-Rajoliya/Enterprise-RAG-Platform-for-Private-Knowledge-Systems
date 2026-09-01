const users = [
 "tenant-admin",
 "rag-user",
 "viewer"
];

export default function UsersTable() {
 return (
  <table>
   <tbody>
    {users.map((u)=>(
     <tr key={u}>
      <td>{u}</td>
     </tr>
    ))}
   </tbody>
  </table>
 );
}