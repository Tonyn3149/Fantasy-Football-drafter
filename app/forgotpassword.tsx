import { router } from "expo-router";
import { Text, TextInput, TouchableOpacity, View } from "react-native";
import { styles } from "./layout";

export default function Index() {
  return (
    <View style={styles.container}>
        <Text style={styles.title}>Password Reset</Text>
                <TextInput 
                    placeholder="Username@gmail.com" 
                    placeholderTextColor="#777"
                    style={styles.username}> 
                </TextInput>
        <TouchableOpacity
            style={styles.button}
            onPress={() => router.push("/login")}
        >
            <Text style={styles.buttonText}>Reset Password</Text>
        </TouchableOpacity>
    </View>
  );
}