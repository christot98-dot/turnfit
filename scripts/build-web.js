const fs=require('fs');fs.rmSync('www',{recursive:true,force:true});fs.mkdirSync('www/icons',{recursive:true});
for(const f of ['index.html','manifest.json','sw.js','logo.png'])fs.copyFileSync(f,'www/'+f);
fs.copyFileSync('icons/icon.svg','www/icons/icon.svg');
