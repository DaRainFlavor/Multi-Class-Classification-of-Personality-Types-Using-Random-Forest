"use client";

import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-[#F5F2E8] text-[#2C2C2C] flex flex-col items-center justify-center p-4 overflow-hidden">
      {/* Decorative shapes */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-10 left-10 w-20 h-20 md:w-32 md:h-32 bg-[#C4A52D] rounded-full opacity-60" />
        <div className="absolute top-40 right-10 md:right-20 w-16 h-16 md:w-24 md:h-24 bg-[#4A7C7C] rounded-full opacity-60" />
        <div className="absolute bottom-20 left-4 md:left-1/4 w-24 h-24 md:w-40 md:h-40 bg-[#8B1538] rounded-full opacity-40" />
        <div className="absolute bottom-40 right-4 md:right-1/3 w-16 h-16 md:w-20 md:h-20 bg-[#C41E3A] rounded-full opacity-50" />
      </div>

      {/* Main content */}
      <div className="relative z-10 max-w-3xl mx-auto text-center w-full">
        {/* Logo/Title */}
        <div className="mb-6 md:mb-8">
          <h1 className="text-4xl sm:text-5xl md:text-7xl font-bold mb-2 md:mb-4 text-[#8B1538]">
            MBTI Quiz
          </h1>
          <p className="text-lg md:text-2xl text-[#4A7C7C] font-medium">
            Discover Your Personality Type
          </p>
        </div>

        {/* Description Card */}
        <div className="bg-white rounded-2xl md:rounded-3xl p-5 md:p-8 mb-6 md:mb-8 shadow-lg border-2 border-[#C4A52D]">
          <p className="text-base md:text-lg text-[#2C2C2C] mb-6 leading-relaxed">
            Take this comprehensive personality assessment based on the Myers-Briggs Type Indicator (MBTI).
            Answer 60 questions to uncover your unique personality type among the 16 possible combinations.
          </p>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4 mb-6">
            <div className="bg-[#8B1538] rounded-xl p-3 md:p-4 text-white">
              <div className="text-2xl md:text-3xl mb-1 md:mb-2">🧠</div>
              <div className="text-sm font-medium">Mind</div>
              <div className="text-xs opacity-80">E / I</div>
            </div>
            <div className="bg-[#4A7C7C] rounded-xl p-3 md:p-4 text-white">
              <div className="text-2xl md:text-3xl mb-1 md:mb-2">👁️</div>
              <div className="text-sm font-medium">Energy</div>
              <div className="text-xs opacity-80">S / N</div>
            </div>
            <div className="bg-[#C4A52D] rounded-xl p-3 md:p-4 text-white">
              <div className="text-2xl md:text-3xl mb-1 md:mb-2">💭</div>
              <div className="text-sm font-medium">Nature</div>
              <div className="text-xs opacity-80">T / F</div>
            </div>
            <div className="bg-[#C41E3A] rounded-xl p-3 md:p-4 text-white">
              <div className="text-2xl md:text-3xl mb-1 md:mb-2">⚡</div>
              <div className="text-sm font-medium">Tactics</div>
              <div className="text-xs opacity-80">J / P</div>
            </div>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-sm text-[#4A7C7C] mb-2 md:mb-6">
            <div className="flex items-center gap-2">
              <span className="text-[#8B1538]">📝</span>
              <span>60 Questions</span>
            </div>
            <div className="hidden sm:block w-1 h-1 rounded-full bg-[#C4A52D]" />
            <div className="flex items-center gap-2">
              <span className="text-[#8B1538]">⏱️</span>
              <span>~10 minutes</span>
            </div>
            <div className="hidden sm:block w-1 h-1 rounded-full bg-[#C4A52D]" />
            <div className="flex items-center gap-2">
              <span className="text-[#8B1538]">🤖</span>
              <span>AI Powered</span>
            </div>
          </div>
        </div>

        {/* CTA Button */}
        <Link
          href="/quiz"
          className="inline-block px-8 py-4 md:px-12 md:py-5 text-lg md:text-xl font-bold rounded-full bg-[#8B1538] text-white hover:bg-[#6B1028] transition-all duration-300 shadow-lg hover:scale-105 transform active:scale-95"
        >
          Start Quiz
        </Link>

        {/* Footer note */}
        <p className="mt-6 md:mt-8 text-xs md:text-sm text-[#4A7C7C] opacity-80">
          Powered by XGBoost Machine Learning Model
        </p>
      </div>
    </main>
  );
}
