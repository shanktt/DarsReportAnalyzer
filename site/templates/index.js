// javascript
// d3.selectAll().data([]).enter().append("p").text(function(d) {return d + ", world";})

var data = [30, 86, 168, 281, 303, 365];

d3.select(".chart")
    .selectAll("div")
    .data(data)
        .enter()
        .append("div")
        .style("width", function(d){ return d + "px"; })
        .text(function(d) { return d; })











// basic bar chart
// var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];

// var svgWidth = 500, svgHeight = 300, barPadding = 5;

// var barWidth = (svgWidth / dataset.length);

// var svg = d3.select("svg")
//         .attr("width", svgWidth)
//         .attr("height", svgHeight);


// var barChart = svg.selectAll("rect")
//         .data(dataset)
//         .enter()
//         .append("rect")
//         .attr("y", function(d){  
//             return svgHeight - d;
//         })
//         .attr("height", function(d){
//             return d;
//         })
//         .attr("width", barWidth - barPadding)
//         .attr("transform", function(d, i){
//             var translate = [barWidth * i, 0];
//             return "translate("+ translate + ")";
//         })
//         .attr("fill", "blue");

// var text = svg.selectAll("text")
//         .data(dataset)
//         .enter()
//         .append("text")
//         .text(function(d) { return d; 
//         })
//         .attr("y", function(d, i){
//             return svgHeight - d - 2;
//         })
//         .attr("x", function(d, i){
//             return barWidth * i;
//         })
//         .attr("fill", "purple");






// d3.select("body")
//     .selectAll("p")
//     .data(stuff)
//     .enter()
//     .append("p")
//     // .text("d3 is cool")
//     .text(function(d){ return d; });

// d3.select("#stuff").style("color", "blue")
// .attr("class", "heading")
// .text("HEY SEXY THANG!!");


// d3.select("body")
//     .append("p")
//     .text("AMEYA YOU SEXY ANIMAL!")
//     .style("color", "aquamarine");
