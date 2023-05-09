import React, { useState, useEffect, useRef } from 'react';
import { Button, View, Text, Image, ScrollView, StyleSheet, TextInput, Pressable, Dimensions, onPress, ImageBackground } from 'react-native';
import { createDrawerNavigator, DrawerContentScrollView } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import CameraRoll from '@react-native-community/cameraroll';
import MenuButtonItem from './components/MenuButtonItem';
import { Searchbar } from 'react-native-paper';
import { MaterialIcons } from '@expo/vector-icons';
import { SafeAreaView } from 'react-native-safe-area-context';
import * as ImagePicker from 'expo-image-picker';
import { Camera } from 'expo-camera';
import { captureRef } from 'react-native-view-shot';

// Import the functions you need from the Firebase SDKs
import { initializeApp } from "firebase/app";
import { getFirestore, collection, doc, getDoc, query, where, getDocs } from 'firebase/firestore';
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';
import { getStorage, ref, uploadBytes } from 'firebase/storage';

// TODO: Replace the following with your app's Firebase project configuration
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
const db = getFirestore(app);
const auth = getAuth(app)
const storage = getStorage(app);
// Render the app component

console.log("Conexión exitosa:", db);

let profesorInfo = null;

const image = { uri: "https://i.ibb.co/MRhBzY9/Login.png" };
const image2 = { uri: "https://i.ibb.co/kBsHbfc/Fondo.png"}; 
const imageback = {uri: "https://cdn-icons-png.flaticon.com/512/32/32170.png?w=1060&t=st=1682023952~exp=1682024552~hmac=8b071115434b9571dd7b8e6dfa30c3199f9644a0cd39895cc98820ddd888154a"};


const styles = StyleSheet.create({

  //Boton Go Back
  header: {
    flexDirection: 'row',
    justifyContent: 'flex-end',
    alignItems: 'center',
    height: 60,
    backgroundColor: '#FFFFFF',
  },
  
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
    marginTop: 200,
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
    marginTop: 5,
    paddingLeft: 20  
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
     <View style={styles.header}>
        <Pressable onPress={() => navigation.navigate('Home')}>
          <MaterialIcons name="arrow-back" size={50} style={{ width: 55, height: 40 }} color="black" />
        </Pressable>
      </View>
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
     <View style={styles.header}>
        <Pressable onPress={() => navigation.navigate('Home')}>
          <MaterialIcons name="arrow-back" size={50} style={{ width: 55, height: 40 }} color="black" />
        </Pressable>
      </View>
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

function Home({ navigation, route }) {
  const [cursos, setCursos] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const { profesorData, userId } = route.params;
  let keyCount = 1; // Iniciamos el contador en 1
  
  useEffect(() => {
    const getCursos = async () => {
      try {
        const cursosRef = collection(db, "curso");
        const q = query(cursosRef, where('id_profesor', '==', userId));
        
        const cursosSnapshot = await getDocs(q);
        const cursosData = cursosSnapshot.docs.map(doc => doc.data());
        setCursos(cursosData);
      } catch (error) {
        console.error(error);
      }
    }
    getCursos();
  }, [profesorData]);

  const onPressCurso = (curso) => {
    navigation.navigate('Classroom', { profesorData: profesorData,
      title: curso.d_nombre + ' ' + curso.d_codigo_seccion,
      body: ['Día: ' + curso.d_dia, 'Horario: ' + curso.z_hora, 'Nro de Alumnos: ' + curso.n_alumnos],
    });
  };
  const filteredCursos = cursos.filter(curso =>
    (curso.d_nombre && curso.d_nombre.toLowerCase().includes(searchQuery.toLowerCase())) ||
    (curso.d_codigo_seccion && curso.d_codigo_seccion.toLowerCase().includes(searchQuery.toLowerCase()))

  );
  return (
    <ScrollView>
    <View>
      <Searchbar
        placeholder="Buscar curso"
        onChangeText={query => setSearchQuery(query)}
        value={searchQuery}
      />
      
      {filteredCursos.map(curso => (
        <Pressable
          key={keyCount++}
          style={styles.buttonhome}
          onPress={() => onPressCurso(curso)}
        >
          <Text style={styles.texttitle}>{curso.d_nombre} {curso.d_codigo_seccion}</Text>
          <Text style={styles.textbody}>Día: {curso.d_dia}</Text>
          <Text style={styles.textbody}>Horario: {curso.z_hora}</Text>
          <Text style={styles.textbtn}>Nro de Alumnos: {curso.n_alumnos}</Text>
        </Pressable>
      ))}
    </View>
    </ScrollView>
  );
}


function Classroom({ navigation, route }) {
  const { profesorData, title, body } = route.params;
  const [cameraPermission, setCameraPermission] = useState(null);
  const [imageUri, setImageUri] = useState(null);

  useEffect(() => {
    getCameraPermission();
  }, []);

  const getCameraPermission = async () => {
    const { status } = await Camera.requestCameraPermissionsAsync();
    setCameraPermission(status === 'granted');
  };

  const takePicture = async () => {
    if (!cameraPermission) {
      console.log('No se concedió permiso para acceder a la cámara.');
      return;
    }
    const { assets } = await ImagePicker.launchCameraAsync({ mediaTypes: ImagePicker.MediaTypeOptions.Images });
    const uri = assets[0].uri;
    console.log(uri);
    setImageUri(uri);
    const imageRef = ref(storage, 'Fotos Subidas/' + Date.now() + '.jpg');
    const response = await fetch(uri);
    const blob = await response.blob();
    const snapshot = await uploadBytes(imageRef, blob);
    console.log('Imagen subida con éxito a Firebase Storage:', snapshot.ref.fullPath);
    
    
  };

  return (
    <View>
      <ImageBackground source={image2} resizeMode="stretch" style={styles.image}>
        <View style={styles.header}>
          <Pressable onPress={() => navigation.navigate('Home', { profesorData: profesorData })}>
            <MaterialIcons name="arrow-back" size={50} style={{ width: 55, height: 40 }} color="black" />
          </Pressable>
        </View>
        <Text style={styles.texttitlec}>{title}</Text>
        {body.map((text, index) => (
          <Text key={index} style={styles.textbodyc}>
            {text}
          </Text>
        ))}
        <View style={styles.containerprofile}>
          <Pressable style={styles.buttonprofile} onPress={takePicture}>
            <Text style={styles.textbtn}>Tomar Foto</Text>
          </Pressable>
        </View>
        {imageUri && (
          <Image source={{ uri: imageUri }} style={{ width: 200, height: 200 }} />
        )}
      </ImageBackground>
    </View>
  );
}


function TabLoginScreen({navigation, setProfesorData}) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const profesorRef = collection(db, "profesor");

  const handleLogin = () => {
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // Usuario inició sesión exitosamente
        const user = userCredential.user;
        //console.log(user);

        // Obtener el documento del profesor correspondiente
        const profesorDoc = doc(profesorRef, user.uid);
        getDoc(profesorDoc).then((doc) => {
          if (doc.exists()) {
            // El documento existe, aquí puedes obtener los datos del profesor
            const data = doc.data();
            setProfesorData(data);
            // Redirigir al usuario a la pantalla "Home"
            navigation.navigate('Home', { profesorData: data, userId: user.uid });
          } else {
            console.log("El documento no existe");
          }
        }).catch((error) => {
          console.log("Error al obtener el documento:", error);
        });
        
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        console.log(errorCode, errorMessage);
      });
    
  }
  return (
  <View style={styles.container}>
    <ImageBackground source={image} resizeMode="stretch" style={styles.image}>
    </ImageBackground>
    <TextInput style={styles.input1}
      placeholder='Email'
      onChangeText={(text) => setEmail(text)}
    />
    <TextInput style={styles.input2}
      placeholder='Contraseña'
      secureTextEntry={true}
      onChangeText={(text) => setPassword(text)}
    />
    <Pressable style={styles.button} onPress={handleLogin}>
      <Text style={styles.text}>Ingresar</Text>
    </Pressable>
    <Pressable onPress={() => navigation.navigate('Cambiar contraseña')}>
      <Text style={styles.subtitle}>¿Has olvidado tu contraseña?</Text>
    </Pressable>
  </View>
 );
}

const MenuItems = ({ navigation }) => {
  return(
    <DrawerContentScrollView
    style = {styles.menuContainer}>
      <Image source = {{uri:"https://i.ibb.co/9V3Y4qk/avatar.jpg"}}
      style = { styles.avatar }/>
      <Text style = {styles.menuTitle}>aaaaaaaaaaa</Text>
      <Text style = {styles.email}>eeeeeeeeeeeee@email.com</Text>
      
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
export default function FaceCounterApp({}) {
  const [profesorData, setProfesorData] = useState(null);
  return (
    <NavigationContainer>
      <Drawer.Navigator
       drawerContent={ (props) => <MenuItems { ...props}/>} 
       initialRouteName="Login"
       screenOptions={{
        headerTintColor: 'white',
        headerStyle: {
          backgroundColor: 'red'
        }
    }}
       >
        <Drawer.Screen options={{headerShown: false}} name="Login">
          {(props) => <TabLoginScreen {...props} setProfesorData={setProfesorData} />}
        </Drawer.Screen>
        <Drawer.Screen name="Home" component={Home}/>
        <Drawer.Screen name="Classroom" component={Classroom} />
        <Drawer.Screen name="Mi Perfil" component={ProfileScreen} />
        <Drawer.Screen name="Ayuda" component={HelpScreen} />
        <Drawer.Screen name="Cambiar contraseña" component={PasswordScreen} />
        <Drawer.Screen options={{headerShown: false}} name="Cerrar Sesión" component={TabLoginScreen} />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}