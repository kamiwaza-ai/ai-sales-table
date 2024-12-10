(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[974],{5068:(e,t,a)=>{Promise.resolve().then(a.bind(a,1128))},1128:(e,t,a)=>{"use strict";a.r(t),a.d(t,{default:()=>j});var s=a(4001),r=a(7749),n=a(3549),o=a(3854);function l(){for(var e=arguments.length,t=Array(e),a=0;a<e;a++)t[a]=arguments[a];return(0,o.QP)((0,n.$)(t))}let d=r.forwardRef((e,t)=>{let{className:a,...r}=e;return(0,s.jsx)("div",{className:"relative w-full overflow-auto",children:(0,s.jsx)("table",{ref:t,className:l("w-full caption-bottom text-sm",a),...r})})});d.displayName="Table";let i=r.forwardRef((e,t)=>{let{className:a,...r}=e;return(0,s.jsx)("thead",{ref:t,className:l("[&_tr]:border-b",a),...r})});i.displayName="TableHeader";let c=r.forwardRef((e,t)=>{let{className:a,...r}=e;return(0,s.jsx)("tbody",{ref:t,className:l("[&_tr:last-child]:border-0",a),...r})});c.displayName="TableBody";let m=r.forwardRef((e,t)=>{let{className:a,...r}=e;return(0,s.jsx)("tr",{ref:t,className:l("border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted",a),...r})});m.displayName="TableRow";let u=r.forwardRef((e,t)=>{let{className:a,...r}=e;return(0,s.jsx)("th",{ref:t,className:l("h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0",a),...r})});u.displayName="TableHead";let h=r.forwardRef((e,t)=>{let{className:a,...r}=e;return(0,s.jsx)("td",{ref:t,className:l("p-4 align-middle [&:has([role=checkbox])]:pr-0",a),...r})});h.displayName="TableCell";let x="https://readme-implementation-app-tunnel-veurtv63.devinapps.com",p={async getData(){let e=await fetch("".concat(x,"/api/data"));if(!e.ok)throw Error("Failed to fetch data");return e.json()},async addColumn(e){if(!(await fetch("".concat(x,"/api/columns"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)})).ok)throw Error("Failed to add column")},async addRow(e){if(!(await fetch("".concat(x,"/api/rows"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({website:e})})).ok)throw Error("Failed to add row")}};class f{connect(){this.ws||(this.ws=new WebSocket("".concat("wss://readme-implementation-app-tunnel-veurtv63.devinapps.com","/ws/updates")),this.ws.onmessage=e=>{try{let t=JSON.parse(e.data);this.onMessage(t)}catch(e){console.error("Failed to parse WebSocket message:",e)}},this.ws.onclose=()=>{this.ws=null,this.scheduleReconnect()},this.ws.onerror=e=>{var t;console.error("WebSocket error:",e),null===(t=this.ws)||void 0===t||t.close()})}scheduleReconnect(){this.reconnectTimeoutId||(this.reconnectTimeoutId=window.setTimeout(()=>{this.reconnectTimeoutId=null,this.connect()},5e3))}disconnect(){var e;this.reconnectTimeoutId&&(window.clearTimeout(this.reconnectTimeoutId),this.reconnectTimeoutId=null),null===(e=this.ws)||void 0===e||e.close(),this.ws=null}constructor(e){this.onMessage=e,this.ws=null,this.reconnectTimeoutId=null}}var b=a(8770);let y=(0,a(8069).F)("inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",{variants:{variant:{default:"bg-primary text-primary-foreground shadow hover:bg-primary/90",destructive:"bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",outline:"border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",secondary:"bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",ghost:"hover:bg-accent hover:text-accent-foreground",link:"text-primary underline-offset-4 hover:underline"},size:{default:"h-9 px-4 py-2",sm:"h-8 rounded-md px-3 text-xs",lg:"h-10 rounded-md px-8",icon:"h-9 w-9"}},defaultVariants:{variant:"default",size:"default"}}),w=r.forwardRef((e,t)=>{let{className:a,variant:r,size:n,asChild:o=!1,...d}=e,i=o?b.DX:"button";return(0,s.jsx)(i,{className:l(y({variant:r,size:n,className:a})),ref:t,...d})});function v(){let[e,t]=(0,r.useState)([]),[a,n]=(0,r.useState)([]),[o,l]=(0,r.useState)(!0),[x,b]=(0,r.useState)(null),y=async()=>{try{let e=await p.getData();t(e.columns),n(e.rows),b(null)}catch(e){b(e instanceof Error?e.message:"Failed to load data")}finally{l(!1)}},v=r.useRef(null);return((0,r.useEffect)(()=>(y(),v.current=new f(e=>{"update"===e.type&&y()}),v.current.connect(),()=>{var e;null===(e=v.current)||void 0===e||e.disconnect()}),[]),o)?(0,s.jsx)("div",{className:"p-8 text-center",children:"Loading..."}):x?(0,s.jsxs)("div",{className:"p-8 text-center",children:[(0,s.jsx)("p",{className:"text-red-500 mb-4",children:x}),(0,s.jsx)(w,{onClick:y,children:"Retry"})]}):(0,s.jsx)("div",{className:"border rounded-lg",children:(0,s.jsxs)(d,{children:[(0,s.jsx)(i,{children:(0,s.jsxs)(m,{children:[(0,s.jsx)(u,{children:"Website"}),e.map(e=>(0,s.jsx)(u,{children:e.name},e.id))]})}),(0,s.jsx)(c,{children:a.map(t=>(0,s.jsxs)(m,{children:[(0,s.jsx)(h,{children:t.website}),e.map(e=>(0,s.jsx)(h,{children:t.data[e.extraction_key]||"-"},"".concat(t.id,"-").concat(e.id)))]},t.id))})]})})}function g(){let[e,t]=(0,r.useState)(!1),[a,n]=(0,r.useState)(null),[o,l]=(0,r.useState)({name:"",extraction_key:""}),d=e=>{let{name:t,value:a}=e.target;l(e=>({...e,[t]:a}))},i=async e=>{e.preventDefault(),t(!0),n(null);try{await p.addColumn({name:o.name,extraction_key:o.extraction_key}),l({name:"",extraction_key:""})}catch(e){n(e instanceof Error?e.message:"Failed to add column")}finally{t(!1)}};return(0,s.jsxs)("div",{className:"p-4 space-y-4 border rounded-lg bg-card",children:[(0,s.jsx)("h2",{className:"text-lg font-semibold",children:"Add New Column"}),(0,s.jsxs)("form",{onSubmit:i,className:"space-y-4",children:[(0,s.jsxs)("div",{className:"space-y-2",children:[(0,s.jsx)("label",{htmlFor:"name",className:"text-sm font-medium",children:"Column Name"}),(0,s.jsx)("input",{id:"name",name:"name",type:"text",required:!0,value:o.name,onChange:d,className:"w-full px-3 py-2 border rounded-md",placeholder:"e.g., Company Size"})]}),(0,s.jsxs)("div",{className:"space-y-2",children:[(0,s.jsx)("label",{htmlFor:"extraction_key",className:"text-sm font-medium",children:"Extraction Key"}),(0,s.jsx)("input",{id:"extraction_key",name:"extraction_key",type:"text",required:!0,value:o.extraction_key,onChange:d,className:"w-full px-3 py-2 border rounded-md",placeholder:"e.g., company_size"})]}),a&&(0,s.jsx)("div",{className:"p-3 text-sm text-red-500 bg-red-50 rounded-md",children:a}),(0,s.jsx)(w,{type:"submit",disabled:e,children:e?"Adding...":"Add Column"})]})]})}function j(){return(0,s.jsxs)("main",{className:"container mx-auto py-8",children:[(0,s.jsx)("h1",{className:"mb-8 text-3xl font-bold",children:"Sales Research Assistant"}),(0,s.jsxs)("div",{className:"mb-8",children:[(0,s.jsx)("h2",{className:"mb-4 text-xl font-semibold",children:"Add New Column"}),(0,s.jsx)(g,{})]}),(0,s.jsxs)("div",{children:[(0,s.jsx)("h2",{className:"mb-4 text-xl font-semibold",children:"Research Data"}),(0,s.jsx)(v,{})]})]})}w.displayName="Button"}},e=>{var t=t=>e(e.s=t);e.O(0,[311,142,767,358],()=>t(5068)),_N_E=e.O()}]);