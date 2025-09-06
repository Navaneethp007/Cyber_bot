'use client';

import Image from 'next/image';
import Link from 'next/link';

interface Feature {
  href: string;
  title: string;
  description: string;
  icon: string;
  gradient: string;
  iconBg: string;
}

const features: Feature[] = [
  {
    href: '/fetch',
    title: 'CVE Data Feed',
    description: 'Access real-time CVE data and vulnerability information with our comprehensive feed',
    icon: '/file.svg',
    gradient: 'from-blue-50 dark:from-blue-900/20',
    iconBg: 'bg-blue-100 dark:bg-blue-900/50'
  },
  {
    href: '/analysis',
    title: 'Threat Analysis',
    description: 'Get in-depth analysis and insights about potential security threats',
    icon: '/window.svg',
    gradient: 'from-purple-50 dark:from-purple-900/20',
    iconBg: 'bg-purple-100 dark:bg-purple-900/50'
  },
  {
    href: '/notify',
    title: 'Notifications',
    description: 'Stay informed with real-time alerts and customizable notifications',
    icon: '/globe.svg',
    gradient: 'from-cyan-50 dark:from-cyan-900/20',
    iconBg: 'bg-cyan-100 dark:bg-cyan-900/50'
  }
];

function FeatureCard({ feature }: { feature: Feature }) {
  return (
    <Link href={feature.href} className="group">
      <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-8 text-center transform transition-all duration-300 hover:scale-105 hover:shadow-xl relative overflow-hidden">
        <div className={`absolute inset-0 bg-gradient-to-br ${feature.gradient} to-transparent opacity-0 group-hover:opacity-100 transition-opacity`} />
        <div className="relative z-10">
          <div className="flex justify-center mb-6">
            <div className={`p-3 ${feature.iconBg} rounded-2xl`}>
              <Image 
                src={feature.icon} 
                alt={feature.title} 
                width={36} 
                height={36} 
                className="transform group-hover:scale-110 transition-transform" 
              />
            </div>
          </div>
          <h2 className="text-xl font-semibold mb-3 text-gray-900 dark:text-white">
            {feature.title}
          </h2>
          <p className="text-gray-600 dark:text-gray-300">
            {feature.description}
          </p>
        </div>
      </div>
    </Link>
  );
}

export default function Home() {
  return (
    <main className="min-h-screen">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center mb-16 max-w-4xl mx-auto">
          <h1 className="text-5xl font-bold mb-6 bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
            Cybersecurity Threat Intelligence Platform
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 mt-4">
            Stay ahead of cyber threats with real-time monitoring, advanced analysis, and instant notifications
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {features.map((feature) => (
            <FeatureCard key={feature.href} feature={feature} />
          ))}
        </div>

        <div className="mt-16 text-center">
          <div className="inline-flex items-center justify-center gap-2 text-sm text-gray-500 dark:text-gray-400 bg-gray-50 dark:bg-gray-800/50 px-4 py-2 rounded-full">
            <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
            </svg>
            Trusted by security professionals worldwide
          </div>
        </div>
      </div>
    </main>
  );
}
