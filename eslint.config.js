import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
// import eslintPluginImport from 'eslint-plugin-import'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      // eslintPluginImport,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
      "quotes": ["error", "double"],
      "semi": ["error", "never"],
      "brace-style": ["error", "1tbs", { "allowSingleLine": true }],
      "comma-dangle": ["error", "always-multiline"],
      "no-trailing-spaces": ["error"],
      "no-multi-spaces": ["error"],
      "prefer-const": ["error"],
      // "eslintPluginImport/order": ["error", {
      //   "newlines-between": "always",
      //   "groups": [
      //     "builtin",
      //     "external",
      //     "internal",
      //     "parent",
      //     "sibling",
      //     "index",
      //     "object",
      //     "type",
      //   ],
      //   "alphabetize": {
      //     "order": "asc",
      //     "caseInsensitive": true,
      //   },
      // }],
    },
    settings: {
      "import/resolver": {
        typescript: {},
      },
    },
  },
)
