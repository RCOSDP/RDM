import js from "@eslint/js"
import stylisticJs from "@stylistic/eslint-plugin-js"
import eslintPluginImportX from "eslint-plugin-import-x"
import reactHooks from "eslint-plugin-react-hooks"
import reactRefresh from "eslint-plugin-react-refresh"
import globals from "globals"
import tseslint from "typescript-eslint"

export default tseslint.config(
  {
    extends: [
      js.configs.recommended,
      ...tseslint.configs.strict,
      ...tseslint.configs.stylistic,
      eslintPluginImportX.flatConfigs.recommended,
      eslintPluginImportX.flatConfigs.typescript,
    ],
    files: ["**/*.{js,ts,tsx}"],
    ignores: ["dist"],
    languageOptions: { ecmaVersion: 2020, globals: globals.browser },
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
      "@stylistic/js": stylisticJs,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      "react-refresh/only-export-components": ["warn", {
        allowConstantExport: true,
      }],

      // Our rules
      "@typescript-eslint/no-non-null-assertion": "off",

      // Stylistic rules
      "@stylistic/js/array-bracket-newline": ["error", "consistent"],
      "@stylistic/js/array-bracket-spacing": ["error", "never"],
      "@stylistic/js/array-element-newline": ["error", "consistent"],
      "@stylistic/js/brace-style": ["error", "1tbs", { allowSingleLine: true }],
      "@stylistic/js/comma-dangle": ["error", "always-multiline"],
      "@stylistic/js/eol-last": ["error", "always"],
      "@stylistic/js/indent": ["error", 2],
      "@stylistic/js/jsx-quotes": ["error", "prefer-double"],
      "@stylistic/js/no-multi-spaces": ["error"],
      "@stylistic/js/no-multiple-empty-lines": ["error", { max: 1 }],
      "@stylistic/js/no-trailing-spaces": ["error"],
      "@stylistic/js/object-curly-newline": ["error", { "consistent": true }],
      "@stylistic/js/object-property-newline": ["error", { allowAllPropertiesOnSameLine: true }],
      "@stylistic/js/object-curly-spacing": ["error", "always"],
      "@stylistic/js/quotes": ["error", "double"],
      "@stylistic/js/semi": ["error", "never"],

      // Import rules
      "import-x/first": "error",
      "import-x/order": ["error", {
        "newlines-between": "always",
        "groups": [
          ["builtin", "external", "internal"],
          "parent",
          "sibling",
          "index",
        ],
        "pathGroups": [
          {
            "pattern": "@/**",
            "group": "internal",
            "position": "after",
          },
        ],
        "pathGroupsExcludedImportTypes": ["builtin"],
        "alphabetize": {
          "order": "asc",
          "caseInsensitive": true,
        },
      }],
      "import-x/newline-after-import": "error",
      "import-x/no-duplicates": "error",
      "import-x/no-unresolved": "off",
    },
  },
)
