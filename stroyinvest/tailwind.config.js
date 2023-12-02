/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/**/*.html'
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
        },
        white: '#fff'
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

