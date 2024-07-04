import { Link } from "react-router-dom"
import { useState, useEffect } from "react"

let ind = -1

export default function SixthFloor() {
    const [update, setUpdate] = useState(0)
    const [temporary, setTemporary] = useState(0)
    const [datas, setDatas] = useState([
        {
            ruang: "RT1",
            servis: "30/12/2022",
            hari: "10 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT2",
            servis: "30/12/2022",
            hari: "20 hari",
            kode: "m",
            status: "off"
        },
        {
            ruang: "RT3",
            servis: "30/12/2022",
            hari: "30 hari",
            kode: "k",
            status: "on"
        },
        {
            ruang: "RT4",
            servis: "30/12/2022",
            hari: "40 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT5",
            servis: "30/12/2022",
            hari: "50 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT6",
            servis: "30/12/2022",
            hari: "60 hari",
            kode: "h",
            status: "off",
        },
        {
            ruang: "RT7",
            servis: "30/12/2022",
            hari: "70 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT8",
            servis: "30/12/2022",
            hari: "90 hari",
            kode: "h",
            status: "off"
        },
        {
            ruang: "RT9",
            servis: "30/12/2022",
            hari: "100 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT10",
            servis: "30/12/2022",
            hari: "110 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT11",
            servis: "30/12/2022",
            hari: "120 hari",
            kode: "h",
            status: "off"
        },
        {
            ruang: "RT12",
            servis: "30/12/2022",
            hari: "130 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT13",
            servis: "30/12/2022",
            hari: "140 hari",
            kode: "h",
            status: "off"
        },
        {
            ruang: "RT14",
            servis: "30/12/2022",
            hari: "150 hari",
            kode: "h",
            status: "on"
        },
        {
            ruang: "RT15",
            servis: "30/12/2022",
            hari: "160 hari",
            kode: "h",
            status: "off"
        },
        {
            ruang: "RT16",
            servis: "30/12/2022",
            hari: "170 hari",
            kode: "h",
            status: "off"
        }
    ])

    useEffect(() => {
        first()
        color(datas)
        const loop = setInterval(() => {
            setUpdate(e => (e == 0 ? 1 : 0))
        }, 1000)
        return () => clearInterval(loop)
    }, [update])

    const first = () => {
        if (temporary == 0) {
            ind = -1
        }
        setTemporary(e => (e == 0 ? 1 : e))
    }

    const changeStatus = (status) => {
        if (ind != -1) {
            if (status != datas[ind].status && datas[ind].kode != "m") {
                colorButton(status)
                setDatas([...datas, datas[ind].status = status])
            }
        }
    }

    return (
        <>
            <div className="container">
                <h1 className="text-floor">Lantai Enam</h1>
            </div>
            <div className="container-two">
                <div className="container-two-one">
                    <div className="container-two-one-two">
                        <ContainerTwoOneTwoOne start={0} value={datas} />
                        <ContainerTwoOneTwoOne start={8} value={datas} />
                    </div>
                </div>
                <div className="container-two-two">
                    <div className="container-two-two-one">
                        <div className="container-two-two-one-one">
                            <p className="information"></p>
                        </div>
                        <div className="container-two-two-one-one">
                            <p className="information"></p>
                        </div>
                        <div className="container-two-two-one-two space-between">
                            <button className="btn" onClick={() => changeStatus("on")}>ON</button>
                            <button className="btn" onClick={() => changeStatus("off")} >OFF</button>
                        </div>
                        <div className="container-two-two-one-two">
                            <Link to="/">
                                <button className="btn absolute">HOME</button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

function ContainerTwoOneTwoOne({ start, value }) {
    return (
        <>
            <div className="container-two-one-two-one">
                <ContainerTwoOneTwoOneOne start={start} value={value} />
                <ContainerTwoOneTwoOneOne start={start + 4} value={value} />
            </div>
        </>
    )
}

function ContainerTwoOneTwoOneOne({ start, value }) {
    return (
        <>
            <div className="container-two-one-two-one-one">
                <Card i={start} value={value} />
                <Card i={start + 1} value={value} />
                <Card i={start + 2} value={value} />
                <Card i={start + 3} value={value} />
            </div>
        </>
    )
}

function Card({ i, value }) {
    const btn = (indeks, msg1, msg2, status, datas) => {
        const info = document.getElementsByClassName('information')
        ind = indeks
        color(datas)
        colorButton(status)
        info[0].innerText = msg1
        info[1].innerText = msg2
    }
    return (
        <>
            <div className="container-two-one-two-one-one-one">
                <div className="container-two-one-two-one-one-one-one">
                    <h1 className="text-info">{value[i].ruang}</h1>
                </div>
                <div className="container-two-one-two-one-one-one-two">
                    <button className="btn-card" onClick={() => btn(i, value[i].servis, value[i].hari, value[i].status, value)}>
                    </button>
                </div>
            </div>
        </>
    )
}

function color(datas) {
    const elemen = document.getElementsByClassName('container-two-one-two-one-one-one')
    Array.from(elemen).map((elemens, idx) => {
        if (idx == ind) {
            elemens.style.backgroundColor = "rgb(255, 255, 255)"
        } else {
            if (datas[idx].kode == "m") {
                elemens.style.backgroundColor = "rgb(255, 146, 139)"
            } else if (datas[idx].kode == "k") {
                elemens.style.backgroundColor = "rgb(255, 250, 139)"
            } else if (datas[idx].kode == "h") {
                elemens.style.backgroundColor = "rgb(155, 255, 139)"
            } else {
                elemens.style.backgroundColor = "rgb(240, 238, 238)"
            }
        }
    })
}

const colorButton = (status) => {
    const btn = document.getElementsByClassName('btn')
    if (status == "on") {
        btn[0].style.backgroundColor = "rgb(155, 255, 139)"
        btn[1].style.backgroundColor = "rgb(240, 238, 238)"
    } else {
        btn[0].style.backgroundColor = "rgb(240, 238, 238)"
        btn[1].style.backgroundColor = "rgb(255, 146, 139)"
    }
}