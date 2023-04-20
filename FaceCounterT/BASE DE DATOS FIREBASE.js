import { getFirestore } from "firebase/firestore";

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBvlvru-JGiHEHKce3e_AFyV3qcpKBBmuo",
  authDomain: "facecounter-7bdad.firebaseapp.com",
  projectId: "facecounter-7bdad",
  storageBucket: "facecounter-7bdad.appspot.com",
  messagingSenderId: "776029603703",
  appId: "1:776029603703:web:7e1070cb34db13f0eec372"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


const db = getFirestore();
console.log("Conexión exitosa:", db);