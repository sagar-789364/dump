# Initialize attribute "skill button clicked"
if "skill_btn_clicked" not in st.session_state:
    st.session_state["skill_btn_clicked"] = False
 
    if st.session_state["skill_btn_clicked"] == True:
 
        session = st.session_state["session"]
 
        result = (
            session.query(SkillsFrequency)
            .filter(
                and_(
                    SkillsFrequency.onet_code == st.session_state["onet_code"],
                    SkillsFrequency.onet_title == str(st.session_state["newTitle"]),
                    SkillsFrequency.category_name != "None",
                    SkillsFrequency.relevant_skill_flag == "1",
                    SkillsFrequency.year == "2019",
                )
            )
            .all()
        )
 
 
