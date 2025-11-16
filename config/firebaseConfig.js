import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDeBH2jXgSRsD1JR78wZ3L-TJky9kOvzLU",
  authDomain: "fantasy-football-drafter-f7129.firebaseapp.com",
  projectId: "fantasy-football-drafter-f7129",
  storageBucket: "fantasy-football-drafter-f7129.firebasestorage.app",
  messagingSenderId: "1004911240200",
  appId: "1:1004911240200:web:ee736ba56c1c23d0b5ddbd",
  measurementId: "G-W1C8Q8HV08"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);