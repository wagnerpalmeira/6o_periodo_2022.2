import React from 'react';
import NavBar from './components/NavBar';
import MyCard from './components/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function App() {

  return (
    <div className="app">
      <NavBar />  
    <Container className='pt-5'>
      <Row>
        <Col md={4}>
            <MyCard title="titulo" text="meu texto" button="Comprar"/>
        </Col>
        <Col md={4}>
            <MyCard title="titulo" text="meu texto" button="Comprar"/>
        </Col>
        <Col md={4}>
            <MyCard title="titulo" text="meu texto" button="Comprar"/>
        </Col>
      </Row>
    </Container>
    </div>
  );
}

export default App;
