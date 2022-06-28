import React, { Component, useState, useEffect } from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import { 
    Box 
} from '@mui/material'


export default function LeagueRouter(props){
    console.log(props.currentLeague.league_id)
    if (props.currentLeague != '') {
        return <Navigate to={'/league/' + props.currentLeague.league_id} />  
    }

    return <Navigate to='/new-league' /> 
}