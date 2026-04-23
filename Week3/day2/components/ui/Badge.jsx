export default function Badge({ children }) {
  return (
    <span className="text-xs px-2 py-1 bg-teal-100 text-teal-700 rounded-full">
      {children}
    </span>
  );
}
