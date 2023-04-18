const nodeLibs = require('node-libs-browser');

module.exports = {
  resolver: {
    extraNodeModules: {
      'crypto': require.resolve('react-native-crypto'),
      'stream': require.resolve('stream-browserify'),
      'util': require.resolve('util/'),
      'assert': require.resolve('assert/'),
      'http': require.resolve('stream-http'),
      'https': require.resolve('https-browserify'),
      'os': require.resolve('os-browserify/browser'),
      'zlib': require.resolve('browserify-zlib'),
      'path': require.resolve('path-browserify'),
      'fs': require.resolve('react-native-level-fs'),
      'vm': require.resolve('vm-browserify')
    },
    sourceExts: ['js', 'jsx', 'ts', 'tsx'], // Agrega aquí cualquier otra extensión de archivo que uses en tu proyecto.
  },
  transformer: {
    babelTransformerPath: require.resolve("react-native-svg-transformer"),
    assetPlugins: ['react-native-svg-transformer']
  }
};

module.exports = nodeLibs;
