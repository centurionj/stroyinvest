/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        blue1: {
          DEFAULT: '#3a677c',
          hover: '#598496',
          10: '#8aa9b7',
          50: '#5e8ea4',
          70: '#49829a'
        },
        gray: {
          1: '#eaeaea',
          2: '#cccccc',
        },
        white: '#fff',
        black: '#000'
      }
    },
  },
  plugins: [],
  safelist: [
    '!bg-blue1',
    'hover:!bg-blue1-hover',
    'text-white',
    'hidden',
  ]
}

