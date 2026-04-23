export default function Input({ className = "", ...props }) {
  return (
    <input
      {...props}
      className={`w-full border px-3 py-2 rounded-lg focus:outline-none ${className}`}
    />
  );
}