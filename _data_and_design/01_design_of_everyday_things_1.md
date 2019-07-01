---
title: Design of Everyday Thoughts - 1
subtitle: Notes from DOET
comments: true
---

This is the first design-related *book* I'm reading. I've read blogs in the past though. 
I picked this up because of its rave reviews and my own interest in wanting to design software and represent data better. 

### Chapter 1 : The psychopathology of everyday things

In the reading of this chapter, Don Norman stresses that the 2 most important characteristics of good design are 

  <!-- <canvas id="canvas" width="800" height="600"></canvas> -->
<svg id="svg"> 
      <!-- <path d="M390,10 Q280,15 150,140" fill="none" stroke="blue" stroke-width="5"/> -->
          <path d="M390,10 C390,10 360,40 250,70" fill="none" stroke="blue" stroke-width="5"/>
          <path d="M390,10 C390,10 420,40 530,70" fill="none" stroke="blue" stroke-width="5"/>
  <ellipse cx="230" cy="130" rx="100" ry="60" fill="transparent" stroke="blue" stroke-width="5"/>
    <text id="svg_text" x="150" y="130" fill="red" font-size="26">DISCOVERABILITY</text>

  <ellipse cx="550" cy="130" rx="100" ry="60" fill="transparent" stroke="blue" stroke-width="5"/>
      <text id="svg_text" x="470" y="130" fill="red" font-size="26">UNDERSTANDING</text>


</svg>
  <script>
    // const rc = rough.canvas(document.getElementById('canvas'));
        const svg = document.getElementById('svg');
    const rc = rough.svg(svg);

   // arcs
    // rc.arc(350, 200, 200, 180, Math.PI, Math.PI * 1.6);
    rc.arc(350, 300, 200, 180, 0, Math.PI/2 );

    //     svg.appendChild(rc.linearPath([[390, 10], [310, 70]], {
    //   roughness: 0.7,
    //   stroke: 'red', strokeWidth: 4
    // }));
    //     svg.appendChild(rc.linearPath([[390, 10], [470, 70]], {
    //   roughness: 0.7,
    //   stroke: 'red', strokeWidth: 4
    // }));



  </script>

