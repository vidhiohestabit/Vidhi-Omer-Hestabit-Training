export default function Button({ children, variant = "primary", className = "" }) {
  const styles = {
    primary: "bg-teal-500 text-white",
    secondary: "bg-gray-200 text-gray-800",
  };

  return (
    <button
      className={`px-4 py-2 rounded-lg hover:bg-amber-900 ${styles[variant]} ${className} `}
    >
      {children}
    </button>
  );
}