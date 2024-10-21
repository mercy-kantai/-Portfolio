import Image from "next/image";
import Header from "./Components/Navbar";
import Hero from "./Components/Hero";
import About from "./Components/About";
import Services from "./Components/Services";
import History from "./Components/History";
import Footer from "./Components/Footer";

export default function Home() {
  return (
  <div>
    <Header/>
    <Hero/>
    <About/>
    <Services/>
    <History/>
    <Footer/>
    </div>
  );
}
