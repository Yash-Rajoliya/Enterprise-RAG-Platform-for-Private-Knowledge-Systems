import UsageChart from "../components/charts/UsageChart";
import CostChart from "../components/charts/CostChart";

export default function Dashboard() {
 return (
  <div>
   <h1>Admin Dashboard</h1>
   <UsageChart />
   <CostChart />
  </div>
 );
}