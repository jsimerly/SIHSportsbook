import React from "react";
import {Navigate, Route} from 'react-router-dom'

export default function AuthCheckRoute(props){
    isLoggedIn = props.user.isLoggedIn

    if (isLoggedIn){
        return (
            <Route
                path={props.path}
                element={props.component}
            />
        )
    } else {
        return <Navigate to='/new-league'/>
    }
}