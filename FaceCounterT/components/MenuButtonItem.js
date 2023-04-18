import { View, Text,TouchableOpacity, StyleSheet, Image } from 'react-native'
import React from 'react'
import {  } from 'react-native'

const MenuButtonItem = ({text,onPress, image}) => {
  return (
    <TouchableOpacity
    style = {styles.buttonContainer}
    onPress={onPress}
    >
        <Image source = {{uri: image}}
        style = { styles.image }/>
    
      <Text style = {styles.buttonText}>{ text }</Text>
    </TouchableOpacity>
  )
}

const styles = StyleSheet.create({
    buttonContainer: {
        alignItems:'center',
        backgroundColor: 'white',
        marginBottom: 10,
        flexDirection: 'row',
        padding:15,
        borderRadius:10,
    },
    buttonText: {
        fontSize: 18,
        marginStart: 7,
        fontWeight: 'bold'
    },
    image: {
        height:25,
        width:25,
    }
})

export default MenuButtonItem