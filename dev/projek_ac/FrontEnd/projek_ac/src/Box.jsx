import axios from 'axios'
import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

export default function Box({ floor, path }) {
    return (
        <>
            <div className='container-lvl'>
                <h1 className='text-lvl'>{floor}</h1>
                <Link to={path}>
                    <div className='lvl' />
                </Link>
            </div>
        </>
    )
} 