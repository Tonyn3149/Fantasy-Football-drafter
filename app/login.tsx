import { router } from "expo-router";
import { Text, TextInput, TouchableOpacity, View } from "react-native";
import { styles } from "./layout";

export default function Login() {
  return (
    <View style={styles.container}>
        <Text style={styles.title}>Sign in</Text>
        <TextInput 
            placeholder="Username@gmail.com" 
            placeholderTextColor="#777"
            style={styles.username}> 
        </TextInput>
        <TextInput 
            placeholder="Password" 
            placeholderTextColor="#777"
            style={styles.password}
            secureTextEntry={true}> 
        </TextInput>

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        style ={styles.button}
        onPress={() => router.push("/forgotpassword")}
        >
        <Text style={styles.buttonText}>Forgot Password</Text>
      </TouchableOpacity>
      
    </View>
  );
}