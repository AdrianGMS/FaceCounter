import React from 'react';
import { Button, View, Text, Image, ScrollView } from 'react-native';
import { createDrawerNavigator, DrawerContentScrollView } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { StyleSheet, TextInput, Pressable, onPress, Dimensions} from 'react-native';
import { ImageBackground } from 'react-native';
import MenuButtonItem from './components/MenuButtonItem';
import { Searchbar } from 'react-native-paper';
import { SafeAreaView } from 'react-native-safe-area-context';
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

const image = { uri: "https://i.ibb.co/MRhBzY9/Login.png" };
const image2 = { uri: "https://i.ibb.co/kBsHbfc/Fondo.png"}; 


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
  input1:{
    backgroundColor: 'white',
    color: 'black',
    fontSize: 18,
    borderWidth: 1,
    borderRadius: 15,
    borderColor: 'white',
    padding: 10,
    width: '80%',
    marginTop: 325,

  },
  input2:{
    backgroundColor: 'white',
    color: 'black',
    fontSize: 18,
    borderWidth: 1,
    borderRadius: 15,
    borderColor: 'white',
    padding: 10,
    width: '80%',
    marginTop: 20,

  },
  //Profile section
  inputprofile:{
    backgroundColor: 'black',
    fontSize:18,
    color:'white',
    width:"92%",
    height:50,
    borderRadius:15,
    padding: 10,
    margin: 15
  },
  buttonprofile:{
    marginTop: 30,
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 15,
    elevation: 3,
    backgroundColor: '#FF2D00',
    alignContent:'center', 
    textAlign:'center',
    alignItems:'center',
    width:"50%", 
    justifyContent:'center', 
    left:"25%"
  },
  buttonpassword:{
    marginTop: 30,
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 15,
    elevation: 3,
    backgroundColor: '#FF2D00',
    width: 165, 
    justifyContent:'center', 
    
    
  },
  textbtn: {
    fontSize: 20,
    lineHeight: 21,
    fontWeight: 'bold',
    color: 'white',
    alignContent:'center',
    textAlign: 'center'
  
  },
  textprofile: {
    fontSize: 15,
    lineHeight: 21,
    letterSpacing: 0.25,
    color: 'black',
    padding: 4,
    marginTop:5,
    paddingLeft:20  
  },
  containerprofile: {
    backgroundColor: 'white'
    
  },
  containerpassword: {
    backgroundColor: 'white',
    paddingHorizontal: 23
    
  
    
  },
  //end profile section
  buttonhome:{
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 15,
    elevation: 3,
    backgroundColor: '#FF2D00',
    margin:20
  },
  texttitle:{
    fontSize:35.5,
    color:'white',
    fontWeight: 'bold',
    textShadowColor:'black',
    textShadowOffset:{width: 0, height: 0},
    textShadowRadius:10 

  },
  texttitlec:{
    fontSize:35.5,
    color:'#f9f7f5',
    fontWeight: 'bold',
    margin:10,
    textShadowColor:'black',
    textShadowOffset:{width: 0, height: 0},
    textShadowRadius:10 
  },
  textbodyc:{
    fontSize:20,
    color:'black',
    margin:10
  },
  textbody:{
    fontSize:20,
    color:'white',
    textAlign:'right',
    marginTop:5
  },
  subtitle:{
    fontSize: 15,
    color: 'white',
    marginTop:35
  },
  image:{
    position: 'absolute',
    left: 0,
    top: 0,
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height,

  },
  image2:{
    position: 'absolute',
    left: 0,
    top: 0,
    width: Dimensions.get('window').width,
    height: 10,

  },
  button:{

    marginTop: 35,
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 15,
    elevation: 3,
    backgroundColor: 'white',
    
  },
  text: {
    fontSize: 15,
    lineHeight: 21,
    fontWeight: 'bold',
    letterSpacing: 0.25,
    color: 'black',
  },
  menuContainer: {
    padding: 15,
  },
  menuTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom:10, 
    color:'white',
    textShadowColor:'black',
    textShadowOffset:{width: 0, height: 0},
    textShadowRadius:10,
  },
  avatar: {
    height: 90,
    width: 90,
    borderRadius:50,
    padding: 15,
    marginBottom: 15
  },
  email:{
    fontSize:14,
    marginBottom:10
  },
  imageToogleMenu: {
    with:10,
    height:10
  },
  searchBar:{
    backgroundColor: '#d9d9d9',
    marginTop: 20,
    marginBottom: 20,
    borderRadius: 15,
    width: '90%',
  },
  passwordInteraction:{
    flexDirection: "row",
    justifyContent: "center",
    
  
  }

});


function PasswordScreen({ navigation }) {
  return (
    <View>
      <ImageBackground source={image2} resizeMode="stretch" style={styles.image}>
     </ImageBackground>
     <Text style={styles.textprofile} >Contraseña Anterior</Text>
      <TextInput style={styles.inputprofile}
      placeholder='ContraseñaAnterior'/>
      <Text style={styles.textprofile}>Nueva Contraseña</Text>
      <TextInput style={styles.inputprofile}
      placeholder='ContraseñaNueva'/>
      <Text style={styles.textprofile}>Repita la Contraseña</Text>
      <TextInput style={styles.inputprofile}
      placeholder='Repitacontraseña'/>
      <View style={styles.passwordInteraction}>
      <View style={styles.containerpassword}>
      <Pressable style={styles.buttonpassword} onPress={() => navigation.navigate('Home')}>
        <Text style={styles.textbtn}>Aceptar</Text>
      </Pressable>
      </View>
      <View style={styles.containerpassword}>
      <Pressable style={styles.buttonpassword} onPress={() => navigation.navigate('Home')}>
        <Text style={styles.textbtn}>Cancelar</Text>
      </Pressable>
      </View>
      </View>
      
    </View>
  );
}
function HelpScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center'}}>
      <ImageBackground source={image2} resizeMode="stretch" style={styles.image}>
     </ImageBackground>
      <Text>AYUDA!</Text>
      <Button 
      onPress={() => navigation.goBack()}
      title="Go back home"
      />
    </View>
  );
}
function ProfileScreen({ navigation }) {
  return (
    <View>
      <ImageBackground source={image2} resizeMode="stretch" style={styles.image}>
     </ImageBackground>
      <Text style={styles.textprofile} >Nombres</Text>
      <TextInput style={styles.inputprofile}
      placeholder='Nombre'/>
      <Text style={styles.textprofile}>Apellidos</Text>
      <TextInput style={styles.inputprofile}
      placeholder='Apellidos'/>
      <Text style={styles.textprofile}>Email</Text>
      <TextInput style={styles.inputprofile}
      placeholder='Email'/>
      <Text style={styles.textprofile}>Numero Telefonico</Text>
      <TextInput style={styles.inputprofile}
      placeholder='Telefono'/>
      <Pressable style={styles.buttonprofile} onPress={() => navigation.navigate('Home')}>
      <Text style={styles.textbtn}>Volver</Text>
    </Pressable>
    </View>
  );
}

function Home({navigation}) {
  return (
    <View>
    <ImageBackground source={image2} resizeMode="stretch" style={styles.image}>
     </ImageBackground>
     <View style={{alignItems: 'center'}}>
     <Searchbar 
      style = {styles.searchBar}
      placeholder="Buscar Aula"
    />
     </View>
     
    <ScrollView>
    <Pressable style={styles.buttonhome} onPress={() => navigation.navigate('Classroom')}>
      <Text style={styles.texttitle}>Programación SW5-964</Text>
      <Text style={styles.textbody}>Día: Lunes</Text>
      <Text style={styles.textbody}>Horario:13-00-15:00</Text>
      <Text style={styles.textbtn}>Nro de Alumnos: 18</Text>
    </Pressable>
    <Pressable style={styles.buttonhome} onPress={() => navigation.navigate('Classroom')}>
      <Text style={styles.texttitle}>Programación SYH-811</Text>
      <Text style={styles.textbody}>Día: Lunes</Text>
      <Text style={styles.textbody}>Horario:13-00-15:00</Text>
      <Text style={styles.textbtn}>Nro de Alumnos: 14</Text>
    </Pressable>
    <Pressable style={styles.buttonhome} onPress={() => navigation.navigate('Classroom')}>
      <Text style={styles.texttitle}>Algoritmos y Estructuras de datos SZ0-395</Text>
      <Text style={styles.textbody}>Día: Martes</Text>
      <Text style={styles.textbody}>Horario:13-00-15:00</Text>
      <Text style={styles.textbtn}>Nro de Alumnos: 20</Text>
    </Pressable>
    <Pressable style={styles.buttonhome} onPress={() => navigation.navigate('Classroom')}>
      <Text style={styles.texttitle}>Complejidad Algoritmica SZZ-980</Text>
      <Text style={styles.textbody}>Día: Lunes</Text>
      <Text style={styles.textbody}>Horario:13-00-15:00</Text>
      <Text style={styles.textbtn}>Nro de Alumnos: 18</Text>
    </Pressable>
    <Pressable style={styles.buttonhome} onPress={() => navigation.navigate('Classroom')}>
      <Text style={styles.texttitle}>IHC SW5-964</Text>
      <Text style={styles.textbody}>Día: Jueves</Text>
      <Text style={styles.textbody}>Horario:13-00-15:00</Text>
      <Text style={styles.textbtn}>Nro de Alumnos: 18</Text>
    </Pressable>
    <Pressable style={styles.buttonhome} onPress={() => navigation.navigate('Classroom')}>
      <Text style={styles.texttitle}>Redes SW5-964</Text>
      <Text style={styles.textbody}>Día: Viernes</Text>
      <Text style={styles.textbody}>Horario:21-00-23:00</Text>
      <Text style={styles.textbtn}>Nro de Alumnos: 18</Text>
    </Pressable>
    </ScrollView>
   
    </View>
  );
}
function Classroom({navigation}){
  return(
    <View>
     <ImageBackground source={image2} resizeMode="stretch" style={styles.image}>
     </ImageBackground>
     <Text style={styles.texttitlec}>Programación SW5-964</Text>
     <Text style={styles.textbodyc}>Nro de Alumnos: 18</Text>
     <Text style={styles.textbodyc}>Día: Lunes</Text>
     <Text style={styles.textbodyc}>Horario: 13:00-15:00  </Text>
     <View style={styles.containerprofile}>
      <Pressable style={styles.buttonprofile} onPress={() => navigation.navigate('Home')}>
        <Text style={styles.textbtn}>Tomar Foto</Text>
      </Pressable>
      </View>
      <View style={styles.containerprofile}>
      <Pressable style={styles.buttonprofile} onPress={() => navigation.navigate('Home')}>
        <Text style={styles.textbtn}>Seleccionar Foto</Text>
      </Pressable>
      </View>
    </View>
  );
}
function TabLoginScreen({navigation}) {
  return (
    
     <View style={styles.container}>
     <ImageBackground source={image} resizeMode="stretch" style={styles.image}>
     </ImageBackground>
    
    
    <TextInput style={styles.input1}
      placeholder='Email'
    />
    <TextInput style={styles.input2}
      placeholder='Contraseña'
      secureTextEntry={true}
    />
    <Pressable style={styles.button} onPress={() => navigation.navigate('Home')}>
    <Text style={styles.text}>Ingresar</Text>
    </Pressable>
    <Pressable onPress={() => navigation.navigate('Cambiar contraseña')}>
    <Text style={styles.subtitle}>¿Has olvidado tu contraseña?</Text>
    </Pressable>

  </View>
  );
}

const MenuItems = ({navigation}) => {
  return(
    <DrawerContentScrollView
    style = {styles.menuContainer}>
      <Image source = {{uri:"https://i.ibb.co/9V3Y4qk/avatar.jpg"}}
      style = { styles.avatar }/>
      <Text style = {styles.menuTitle}>Usuario Profesor Prueba</Text>
      <Text style = {styles.email}>usuarioprofesorprueba@qwerty.com</Text>
      
      <MenuButtonItem
        image='https://i.ibb.co/R2Bqyf0/Home.png'
        text ="Home"
        onPress={() => navigation.navigate('Home')}/>
        <MenuButtonItem
        image='https://i.ibb.co/pKZQsf8/Perfil.png'
        text ="Mi Perfil"
        onPress={() => navigation.navigate('Mi Perfil')}/>
        <MenuButtonItem
        image='https://i.ibb.co/CvPSX89/Ayuda.png'
        text ="Ayuda"
        onPress={() => navigation.navigate('Ayuda')}/>
        <MenuButtonItem
        image='https://i.ibb.co/qCmQ03M/Cambiar-contrase-a.png'
        text ="Cambiar contraseña"
        onPress={() => navigation.navigate('Cambiar contraseña')}/>
        <MenuButtonItem
        image='https://i.ibb.co/z2hvrff/cerrar-sesion.png'
        text ="Cerrar Sesión"
        onPress={() => navigation.navigate('Cerrar Sesión')}/>
    </DrawerContentScrollView>
  )

}


const Drawer = createDrawerNavigator();
export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator
       drawerContent={ (props) => <MenuItems { ...props} />} 
       initialRouteName="Login"
       screenOptions={{
        headerTintColor: 'white',
        headerStyle: {
          backgroundColor: 'red'
        }
    }}
       >
        <Drawer.Screen options={{headerShown: false}} name="Login" component={TabLoginScreen} />
        <Drawer.Screen name="Home" component={Home} />
        <Drawer.Screen name="Classroom" component={Classroom} />
        <Drawer.Screen name="Mi Perfil" component={ProfileScreen} />
        <Drawer.Screen name="Ayuda" component={HelpScreen} />
        <Drawer.Screen name="Cambiar contraseña" component={PasswordScreen} />
        <Drawer.Screen options={{headerShown: false}} name="Cerrar Sesión" component={TabLoginScreen} />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}