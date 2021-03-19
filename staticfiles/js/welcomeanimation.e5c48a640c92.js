const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".text", { y: "0%", duration: 0.75, stagger: 0.5 });
tl.to(".slider", { y: "-100%", duration: 1, delay: 0.5 });
tl.to(".intro", { y: "-100%", duration: 1 }, "-=1");
tl.fromTo("nav", { opacity: 0 }, { opacity: 1, duration: 1 });
tl.fromTo(".profile_picture,h2,.pwelcome,#hi-background", { opacity: 0 }, { opacity: 1, duration: 0.5 });
tl.fromTo("h3,h4,hr,table,.h1edit,.picture-tx,.link,.picture_caption,.picture,.tuns,footer,.maincontentanimation", { opacity: 0 }, { opacity: 1, duration: 0.5 });
tl.fromTo(".big-text", { opacity: 0 }, { opacity: 1, duration: 0.5 }, "-=1");