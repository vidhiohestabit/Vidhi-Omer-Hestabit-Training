export default function DashboardLayout({ children }) {
  return (
    <section>
      <h2 className="text-2xl font-semibold mb-4">Dashboard</h2>
      {children}
    </section>
  );
}
