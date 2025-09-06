interface DataCardProps {
  title: string;
  children: React.ReactNode;
  className?: string;
  isLoading?: boolean;
}

export default function DataCard({ title, children, className = '', isLoading = false }: DataCardProps) {
  return (
    <div className={`
      bg-white dark:bg-gray-800 
      rounded-xl shadow-sm 
      border border-gray-200 dark:border-gray-700
      overflow-hidden
      transition-all duration-200
      hover:shadow-md
      ${className}
    `}>
      <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700 flex items-center justify-between">
        <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-200">
          {title}
        </h2>
        {isLoading && (
          <div className="animate-spin rounded-full h-5 w-5 border-2 border-gray-300 dark:border-gray-600 border-t-blue-600"></div>
        )}
      </div>
      <div className="p-6 bg-white dark:bg-gray-800">
        {isLoading ? (
          <div className="animate-pulse space-y-4">
            <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-3/4"></div>
            <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-1/2"></div>
          </div>
        ) : (
          <div className="text-gray-600 dark:text-gray-300">{children}</div>
        )}
      </div>
    </div>
  );
}
