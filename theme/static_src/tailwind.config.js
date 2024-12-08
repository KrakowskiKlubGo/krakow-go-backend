/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    daisyui: {
        themes: [
            {
                kkg: {
                    "primary": "#42a5f5",
                    "primary-content": "#010a15",
                    "secondary": "#ab47bc",
                    "secondary-content": "#f0dbf3",
                    "accent": "#d32f2f",
                    "accent-content": "#fcd9d5",
                    "neutral": "#1e1e1e",
                    "neutral-content": "#fff",
                    "base-100": "#1e1e1e",
                    "base-200": "#0e0e0e",
                    "base-300": "#0a0a0a",
                    "base-content": "#fff",
                    "info": "#0288d1",
                    "info-content": "#000610",
                    "success": "#388e3c",
                    "success-content": "#010701",
                    "warning": "#f57c00",
                    "warning-content": "#150500",
                    "error": "#d32f2f",
                    "error-content": "#fcd9d5",
                    "--rounded-box": "0.5rem",
                },
            }
        ],
        base: false, // applies background color and foreground color for root element by default
        styled: true, // include daisyUI colors and design decisions for all components
        utils: true, // adds responsive and modifier utility classes
        prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
        logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
        themeRoot: ":root", // The element that receives theme color CSS variables
    },
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'


    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Varela Round', 'sans-serif'],
                mono: ['Varela Round', 'sans-serif'],
                serif: ['Varela Round', 'sans-serif'],
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
}
